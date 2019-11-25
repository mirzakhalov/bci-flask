import asyncio
from lib.cortex import Cortex


async def do_stuff(cortex):
    await cortex.get_user_login()
    await cortex.get_cortex_info()
    await cortex.has_access_right()
    await cortex.request_access()
    await cortex.authorize()
    await cortex.get_license_info()
    await cortex.query_headsets()
    if len(cortex.headsets) > 0:
        await cortex.create_session(activate=True,
                                    headset_id=cortex.headsets[0])
        await cortex.create_record(title="test record 1")
        await cortex.subscribe(['pow'])
        while cortex.packet_count < 10: # modify this loop to get more readings
            await cortex.get_data()
        await cortex.close_session()


def test():
    cortex = Cortex('./cortex_creds')
    asyncio.run(do_stuff(cortex))
    cortex.close()


if __name__ == '__main__':
    test()
