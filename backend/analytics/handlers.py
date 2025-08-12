import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
from typing import List, Dict, Any

def statistics(data:dict):
    expenses = data.get("expenses")
    incomes = data.get("incomes")
    if not expenses or not incomes:
        return None
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

    max_month_expense = last_month_expenses["value"].max()
    max_year_expense = last_year_expenses["value"].max()
    max_expense = expenses_df["value"].max()
    ballance = total_profit

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
            },
            "max_month_expense":max_month_expense,
            "max_year_expense":max_year_expense,
            "max_expense":max_expense,
            "ballance":ballance
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



def _create_pie_chart(data: pd.DataFrame, title: str, ax) -> None:
    if not data.empty:
        pie_data = data.groupby("category")["value"].sum()
        pie_data.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            colormap="Pastel1" if "Расходы" in title else "Pastel2",
            ylabel="",
            ax=ax,
            title=title
        )
    else:
        ax.set_title(f"Нет данных для {title.lower()}")
        ax.axis('off')

def _create_line_chart(data: pd.DataFrame, title: str, ax) -> None:
    if not data.empty:
        trends_data = data.groupby([pd.Grouper(key="created_at", freq="D"), "category"])["value"].sum().reset_index()
        sns.lineplot(
            data=trends_data,
            x="created_at",
            y="value",
            hue="category",
            marker="o",
            ax=ax
        )
        ax.set_title(title)
        ax.set_ylabel("Сумма")
        ax.set_xlabel("Дата")
        ax.grid(True, alpha=0.3)
        ax.legend(title="Категории", bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        ax.set_title(f"Нет данных для {title.lower()}")
        ax.axis('off')

def visualization(data: Dict[str, List[Dict[str, Any]]]) -> List[bytes]:
    
    incomes_df = pd.DataFrame(data.get("incomes", []))
    expenses_df = pd.DataFrame(data.get("expenses", []))

    today = pd.Timestamp.now()
    one_year_ago = today - pd.DateOffset(years=1)
    one_month_ago = today - pd.DateOffset(months=1)

    plots_bytes: List[bytes] = []

    if not incomes_df.empty:
        incomes_df["created_at"] = pd.to_datetime(incomes_df["created_at"]).dt.tz_localize(None)
        incomes_df = incomes_df.dropna(subset=["category", "value"])
    
    if not expenses_df.empty:
        expenses_df["created_at"] = pd.to_datetime(expenses_df["created_at"]).dt.tz_localize(None)
        expenses_df = expenses_df.dropna(subset=["category", "value"])

    last_year_incomes = incomes_df[incomes_df.created_at > one_year_ago] if not incomes_df.empty else pd.DataFrame()
    last_month_incomes = incomes_df[incomes_df.created_at > one_month_ago] if not incomes_df.empty else pd.DataFrame()
    last_year_expenses = expenses_df[expenses_df.created_at > one_year_ago] if not expenses_df.empty else pd.DataFrame()
    last_month_expenses = expenses_df[expenses_df.created_at > one_month_ago] if not expenses_df.empty else pd.DataFrame()

    pie_data = [
        (incomes_df, "Доходы за всё время"),
        (expenses_df, "Расходы за всё время"),
        (last_year_incomes, "Доходы за год"),
        (last_year_expenses, "Расходы за год"),
        (last_month_incomes, "Доходы за месяц"),
        (last_month_expenses, "Расходы за месяц"),
    ]

    for df, title in pie_data:
        fig, ax = plt.subplots(figsize=(8, 8))
        _create_pie_chart(df, title, ax)
        img_buffer = io.BytesIO()
        fig.savefig(img_buffer, format="png")
        img_buffer.seek(0)
        plots_bytes.append(img_buffer.getvalue())
        plt.close(fig)

    line_data = [
        (incomes_df, "Динамика доходов за всё время"),
        (expenses_df, "Динамика расходов за всё время"),
        (last_year_incomes, "Динамика доходов за год"),
        (last_year_expenses, "Динамика расходов за год"),
        (last_month_incomes, "Динамика доходов за месяц"),
        (last_month_expenses, "Динамика расходов за месяц"),
    ]

    for df, title in line_data:
        fig, ax = plt.subplots(figsize=(15, 8))
        _create_line_chart(df, title, ax)
        plt.tight_layout()
        img_buffer = io.BytesIO()
        fig.savefig(img_buffer, format="png")
        img_buffer.seek(0)
        plots_bytes.append(img_buffer.getvalue())
        plt.close(fig)

    return plots_bytes