from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from ..activities.demo import demo_activity


@workflow.defn
class DemoWorkflow:
    @workflow.run
    async def run(self, a: int, b: int) -> int:
        return await workflow.execute_activity(
            demo_activity,
            args=[a, b],
            start_to_close_timeout=timedelta(seconds=30),
        )
