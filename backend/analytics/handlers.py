import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io


def statistics(data:dict):
    expenses = data["expenses"]
    incomes = data["incomes"]

    expenses_df = pd.DataFrame(expenses)
    incomes_df = pd.DataFrame(incomes)

    expenses_df["created_at"] = pd.to_datetime(expenses_df["created_at"]).dt.tz_localize(None)
    incomes_df["created_at"] = pd.to_datetime(incomes_df["created_at"]).dt.tz_localize(None)

    expenses_df["updated_at"] = pd.to_datetime(expenses_df["updated_at"]).dt.tz_localize(None)
    incomes_df["updated_at"] = pd.to_datetime(incomes_df["updated_at"]).dt.tz_localize(None)

    today = pd.Timestamp.now()
    one_year_ago = today - pd.DateOffset(years=1)
    one_month_ago = today - pd.DateOffset(months=1)



    last_year_expenses = expenses_df[expenses_df.created_at > one_year_ago]
    last_year_incomes = incomes_df[incomes_df.created_at > one_year_ago]

    last_month_expenses = expenses_df[expenses_df.created_at > one_month_ago]
    last_month_incomes = incomes_df[incomes_df.created_at > one_month_ago]

    all_incomes = incomes_df
    all_expenses = expenses_df



    total_month_incomes = last_month_incomes["value"].sum()
    total_month_expenses = last_month_expenses["value"].sum()
    total_month_profit = total_month_incomes - total_month_expenses

    total_year_incomes= last_year_incomes["value"].sum()
    total_year_expenses = last_year_expenses["value"].sum()
    total_year_profit = total_year_incomes - total_year_expenses

    total_incomes = incomes_df["value"].sum()
    total_expenses = expenses_df["value"].sum()
    total_profit = total_incomes - total_expenses

    return {
        "expenses":{
            "records":{
                "all_expenses_records":all_expenses.to_dict(orient='records'),
                "last_year_expenses_records":last_year_expenses.to_dict(orient='records'),
                "last_month_expenses_records":last_month_expenses.to_dict(orient='records')
            },
            "total":{
                "total_expenses":total_expenses,
                "total_year_expenses":total_year_expenses,
                "total_month_expenses":total_month_expenses
            }
        },
        "incomes":{
            "records":{
                "all_income_records":all_incomes.to_dict(orient='records'),
                "last_year_income_records":last_year_incomes.to_dict(orient='records'),
                "last_month_income_records":last_month_incomes.to_dict(orient='records')
            },
            "total":{
                "total_incomes":total_incomes,
                "total_year_incomes":total_year_incomes,
                "total_month_incomes":total_month_incomes
            }
        },
        "profit":{
            "total":{
                "total_profit":total_profit,
                "total_year_profit":total_year_profit,
                "total_month_profit":total_month_profit
            }
        }
    }




def visualization(data: dict):
    incomes_df = pd.DataFrame(data["incomes"])
    expenses_df = pd.DataFrame(data["expenses"])


    if not incomes_df.empty:
        incomes_df["created_at"] = pd.to_datetime(incomes_df["created_at"])
        incomes_df = incomes_df.dropna(subset=["category", "value"])
    
    if not expenses_df.empty:
        expenses_df["created_at"] = pd.to_datetime(expenses_df["created_at"])
        expenses_df = expenses_df.dropna(subset=["category", "value"])
        
    incomes_pie_data = incomes_df.groupby("category")["value"].sum()
    expenses_pie_data = expenses_df.groupby("category")["value"].sum()

    incomes_trends_grouped = incomes_df.groupby([pd.Grouper(key="created_at", freq="D"), "category"])["value"].sum().reset_index()
    expenses_trends_grouped = expenses_df.groupby([pd.Grouper(key="created_at", freq="D"), "category"])["value"].sum().reset_index()


    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    if not incomes_pie_data.empty:
        incomes_pie_data.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            colormap="Pastel2",
            ylabel="",
            ax=axes[0, 0],
            title="Доходы по категориям"
        )
    else:
        axes[0, 0].set_title("Нет данных о доходах")
    
    if not expenses_pie_data.empty:
        expenses_pie_data.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            colormap="Pastel1",
            ylabel="",
            ax=axes[0, 1],
            title="Расходы по категориям"
        )
    else:
        axes[0, 1].set_title("Нет данных о расходах")

    if not incomes_trends_grouped.empty:
        sns.lineplot(
            data=incomes_trends_grouped,
            x="created_at",
            y="value",
            hue="category",
            marker="o",
            ax=axes[1, 0]
        )
        axes[1, 0].set_title("Динамика доходов")
        axes[1, 0].set_ylabel("Сумма")
        axes[1, 0].set_xlabel("Дата")
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].legend(title="Категории", bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        axes[1, 0].set_title("Нет данных для трендов доходов")

    if not expenses_trends_grouped.empty:
        sns.lineplot(
            data=expenses_trends_grouped,
            x="created_at",
            y="value",
            hue="category",
            marker="o",
            ax=axes[1, 1]
        )
        axes[1, 1].set_title("Динамика расходов")
        axes[1, 1].set_ylabel("Сумма")
        axes[1, 1].set_xlabel("Дата")
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].legend(title="Категории", bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        axes[1, 1].set_title("Нет данных для трендов расходов")

    plt.suptitle("Аналитика доходов и расходов", fontsize=20, y=0.95)
    plt.tight_layout(rect=(0, 0, 1, 0.9))
    
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    plt.close(fig)
    
    return img_buffer.getvalue()