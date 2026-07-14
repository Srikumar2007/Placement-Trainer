import asyncio
import os
import sys
import inspect

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

async def test_startup():
    from backend.main import app
    from backend.database import get_database
    
    print("Testing startup handlers...")
    for handler in app.router.on_startup:
        try:
            if inspect.iscoroutinefunction(handler):
                await handler()
            else:
                handler()
            print(f"Handler {handler.__name__} success")
        except Exception:
            print(f"Handler {handler.__name__} failed:")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_startup())
