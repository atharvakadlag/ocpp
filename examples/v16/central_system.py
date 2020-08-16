import asyncio
import logging
from datetime import datetime

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    sys.exit(1)

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import Action, RegistrationStatus
from ocpp.v16 import call_result, call

logging.basicConfig(level=logging.ERROR)

class ChargePoint(cp):
    # initiated  by charge point
    @on(Action.BootNotification)
    def on_boot_notitication(self, charge_point_vendor, charge_point_model, **kwargs):
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted
        )
    
    @on(Action.Heartbeat)
    def on_heartbeat(self, **kwargs):
        """
        This contains the field definition of the Heartbeat.conf PDU sent by the Central System
        to the Charge Point in response to a Heartbeat.req PDU.
        """
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().isoformat()
        )

    @on(Action.FirmwareStatusNotification)
    def on_firmware_status_notification(self, status, **kwargs):
        """
        This contains the field definition of the FirmwareStatusNotification.conf PDU
        sent by the Central System to the Charge Point in response to
        a FirmwareStatusNotification.req PDU.
        """

        return call_result.FirmwareStatusNotificationPayload()

    @on(Action.StatusNotification)
    def on_status_notification(self, status, **kwargs):
        """
        This contains the field definition of the FirmwareStatusNotification.conf PDU
        sent by the Central System to the Charge Point in response to
        a FirmwareStatusNotification.req PDU.
        """

        return call_result.StatusNotificationPayload()

    @on(Action.MeterValues)
    def on_meter_values(self, connectorId, transaction_id, meter_value, **kwargs):
        return call_result.MeterValuesPayload()

    # initiated by central system
    async def send_cancel_reservation(self):
        """
        This contains the field definition of the CancelReservation.req PDU
        sent by the Central System to the Charge Point
        """
        request = call.CancelReservation(
            reservation_id = 1
        )

        response = await self.call(request)

async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint instance
    and start listening for messsages.

    """
    charge_point_id = path.strip('/')
    cp = ChargePoint(charge_point_id, websocket)

    await cp.start()


async def main():
    server = await websockets.serve(
        on_connect,
        '0.0.0.0',
        9000,
        subprotocols=['ocpp1.6']
    )

    await server.wait_closed()


if __name__ == '__main__':
    try:
        # asyncio.run() is used when running this example with Python 3.7 and
        # higher.
        asyncio.run(main())
    except AttributeError:
        # For Python 3.6 a bit more code is required to run the main() task on
        # an event loop.
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
