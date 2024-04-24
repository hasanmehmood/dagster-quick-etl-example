from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_package_module,
    job,
    op,
    graph,
    Nothing,
    In,
)
import pandas as pd

@op
def my_op():
    # create a pandas dataframe
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    # print the dataframe
    print(df)

    print("My first job printing a dataframe!")


@op(ins={"start": In(Nothing)})
def my_second_op():
    print("This is my second job")


@job
def my_job():
    my_op()


@job
def my_seocnd_job():
    my_second_op()


@graph
def nothing_dependency():
    my_second_op(start=my_op())



# Define jobs from graph
nothing_dependency_job = nothing_dependency.to_job()

nothing_dependency_schedule = ScheduleDefinition(
    job=nothing_dependency_job,
    cron_schedule="*/1 * * * *",  # Run daily at 6:00 PM
)

# daily_refresh_schedule = ScheduleDefinition(job=my_job, cron_schedule="*/1 * * * *")

# daily_refresh_schedule_second = ScheduleDefinition(
#     job=my_seocnd_job,
#     cron_schedule="*/1 * * * *",
# )

defs = Definitions(schedules=[nothing_dependency_schedule])
