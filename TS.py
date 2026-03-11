import asyncio

async def say_after(delay, word):
    await asyncio.sleep(delay)
    print(word)

async def main():
    # 'async with' handles the group lifecycle
    async with asyncio.TaskGroup() as tg:
        # 'create_task' adds tasks to this specific group
        tg.create_task(say_after(1, "hello"))
        tg.create_task(say_after(2, "world"))
    
    # Execution only reaches here after BOTH tasks are finished
    print("Tasks complete!")

asyncio.run(main())
