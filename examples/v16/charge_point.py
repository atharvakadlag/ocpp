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
from ocpp.v16.enums import Action, RegistrationStatus, FirmwareStatus, ChargePointErrorCode, ChargePointStatus, CancelReservationStatus
from ocpp.v16 import call, call_result

logging.basicConfig(level=logging.ERROR)


class ChargePoint(cp):
    def __init__(self, id, connection, response_timeout=30):
        super().__init__(id, connection, response_timeout=response_timeout)
        self.charge_point_vendor = "Tesla"
        self.charge_point_models = "Optimus"

    # operations inititated by the central system
    @on(Action.CancelReservation)    
    def on_cancel_resrvation(self, resrvation_id, **kwargs):
        """

        """

        return call_result.CancelReservationPayload(
            status = CancelReservationStatus.accepted
        )
    # operations inititated by charge point 
    
    async def send_boot_notification(self):
        request = call.BootNotificationPayload(
            charge_point_model= self.charge_point_models,
            charge_point_vendor= self.charge_point_vendor,
        )

        response = await self.call(request)

        if response.status ==  RegistrationStatus.accepted:
            print("Connected to central system.")

    async def send_heartbeart(self):
        """
        This contains the field definition of the Heartbeat.req PDU sent by
        the Charge Point to the Central System. See also Heartbeat
        No fields are defined.
        """

        request = call.HeartbeatPayload()

        response = await self.call(request)

        print(response.current_time)

    async def send_firmware_status_notification(self):
        """
        This contains the field definition of the FirmwareStatusNotifitacion.req PDU
        sent by the Charge Point to the Central System.
        """

        request = call.FirmwareStatusNotificationPayload(
            #TODO not sure what status  means
            status = FirmwareStatus.installed,
        )

        response = await self.call(request)

        print(response)

    async def send_status_notification(self):
        """
        This  contains  the  field  definition  of  the  StatusNotification.req  PDU 
        sent  by  the  Charge  Point  to  theCentral System.
        """

        request = call.StatusNotificationPayload(
            connector_id = 2,
            error_code = ChargePointErrorCode.noError,
            status = ChargePointStatus.available,
        )

        response = await self.call(request)

        print(response)

    async def send_data_transfer(self):

        request = call.DataTransferPayload(
            vendor_id = self.charge_point_vendor,
        )

        response = await self.call(request)

    async def send_meter_value(self):
        request = call.MeterValuesPayload(
            connectorId = 1,
            transaction_id = 12345678,
            meter_value = [{
                'sampledValue': [{
                    "value": "50.0",
                    "measurand": "Frequency",
                    "unit": "Hertz",
                }]
            }]
        )

        response = await self.call(request)


async def main():
    async with websockets.connect(
        'ws://localhost:9000/CP_1',
         subprotocols=['ocpp1.6']
    ) as ws:

        cp = ChargePoint('CP_1', ws)

        await asyncio.gather(
            cp.start(),
            cp.send_boot_notification(),
            cp.heartbeart_req(),
        )


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
