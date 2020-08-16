from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class AuthorizePayload:
    id_token: Dict
    _15118_certificate_hash_data: List = None
    evse_id: List = None


@dataclass
class BootNotificationPayload:
    charging_station: Dict
    reason: str


@dataclass
class CancelReservationPayload:
    reservation_id: int


@dataclass
class CertificateSignedPayload:
    cert: List
    type_of_certificate: str = None


@dataclass
class ChangeAvailabilityPayload:
    evse_id: int
    operational_status: str


@dataclass
class ClearCachePayload:
    pass


@dataclass
class ClearChargingProfilePayload:
    evse_id: int = None
    charging_profile: Dict = None


@dataclass
class ClearDisplayMessagePayload:
    id: int


@dataclass
class ClearVariableMonitoringPayload:
    id: List


@dataclass
class ClearedChargingLimitPayload:
    charging_limit_source: str
    evse_id: int = None


@dataclass
class CostUpdatedPayload:
    total_cost: int
    transaction_id: str


@dataclass
class CustomerInformationPayload:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Dict = None
    id_token: Dict = None
    customer_identifier: str = None


@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: str = None
    data: Any = None


@dataclass
class DeleteCertificatePayload:
    certificate_hash_data: Dict


@dataclass
class FirmwareStatusNotificationPayload:
    status: str
    request_id: int


@dataclass
class Get15118EVCertificatePayload:
    _15118_schema_version: str
    exi_request: str


@dataclass
class GetBaseReportPayload:
    request_id: int
    report_base: str


@dataclass
class GetCertificateStatusPayload:
    ocsp_request_data: Dict


@dataclass
class GetChargingProfilesPayload:
    charging_profile: Dict
    request_id: int = None
    evse_id: int = None


@dataclass
class GetCompositeSchedulePayload:
    duration: int
    evse_id: int
    charging_rate_unit: str = None


@dataclass
class GetDisplayMessagesPayload:
    request_id: int
    priority: str = None
    state: str = None
    id: List = None


@dataclass
class GetInstalledCertificateIdsPayload:
    type_of_certificate: str


@dataclass
class GetLocalListVersionPayload:
    pass


@dataclass
class GetLogPayload:
    log: Dict
    log_type: str
    request_id: int
    retries: int = None
    retry_interval: int = None


@dataclass
class GetMonitoringReportPayload:
    component_variable: List = None
    request_id: int = None
    monitoring_criteria: List = None


@dataclass
class GetReportPayload:
    component_variable: List = None
    request_id: int = None
    component_criteria: List = None


@dataclass
class GetTransactionStatusPayload:
    transaction_id: str = None


@dataclass
class GetVariablesPayload:
    get_variable_data: List


@dataclass
class HeartbeatPayload:
    pass


@dataclass
class InstallCertificatePayload:
    certificate_type: str
    certificate: str


@dataclass
class LogStatusNotificationPayload:
    status: str
    request_id: int


@dataclass
class MeterValuesPayload:
    evse_id: int
    meter_value: List


@dataclass
class NotifyCentralChargingNeedsPayload:
    evse_id: int
    sa_schedule: List


@dataclass
class NotifyChargingLimitPayload:
    charging_limit: Dict
    charging_schedule: List = None
    evse_id: int = None


@dataclass
class NotifyCustomerInformationPayload:
    data: str
    tbc: bool
    seq_no: int
    generated_at: str
    request_id: int = None


@dataclass
class NotifyDisplayMessagesPayload:
    message_info: List
    request_id: int
    tbc: bool


@dataclass
class NotifyEVChargingNeedsPayload:
    charging_needs: Dict
    evse_id: int
    max_schedule_tuples: int = None


@dataclass
class NotifyEVChargingSchedulePayload:
    time_base: str
    charging_schedule: Dict
    evse_id: int


@dataclass
class NotifyEventPayload:
    generated_at: str
    tbc: bool
    seq_no: int
    event_data: List


@dataclass
class NotifyMonitoringReportPayload:
    monitor: List
    tbc: bool
    seq_no: int
    generated_at: str
    request_id: int = None


@dataclass
class NotifyReportPayload:
    generated_at: str
    report_data: List
    tbc: bool
    seq_no: int
    request_id: int = None


@dataclass
class PublishFirmwarePayload:
    location: str
    checksum: str
    retries: int = None


@dataclass
class PublishFirmwareStatusNotificationPayload:
    status: str
    location: str = None


@dataclass
class Renegotiate15118SchedulePayload:
    evse: Dict


@dataclass
class ReportChargingProfilesPayload:
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    request_id: int = None
    tbc: bool = None


@dataclass
class RequestStartTransactionPayload:
    id_token: Dict
    remote_start_id: int
    evse_id: int = None
    charging_profile: Dict = None


@dataclass
class RequestStopTransactionPayload:
    transaction_id: str


@dataclass
class ReservationStatusUpdatePayload:
    reservation_id: int
    reservation_update_status: str


@dataclass
class ReserveNowPayload:
    id_token: Dict
    reservation: Dict
    group_id_token: Dict = None


@dataclass
class ResetPayload:
    type: str


@dataclass
class SecurityEventNotificationPayload:
    type: str
    timestamp: str


@dataclass
class SendLocalListPayload:
    version_number: int
    update_type: str
    local_authorization_list: List = None


@dataclass
class SetChargingProfilePayload:
    evse_id: int
    charging_profile: Dict


@dataclass
class SetDisplayMessagePayload:
    message: Dict


@dataclass
class SetMonitoringBasePayload:
    monitoring_base: str


@dataclass
class SetMonitoringLevelPayload:
    severity: int


@dataclass
class SetNetworkProfilePayload:
    configuration_slot: int
    connection_data: Dict


@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_data: List


@dataclass
class SetVariablesPayload:
    set_variable_data: List


@dataclass
class SignCertificatePayload:
    csr: str
    type_of_certificate: str = None


@dataclass
class StatusNotificationPayload:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int


@dataclass
class TransactionEventPayload:
    event_type: str
    timestamp: str
    trigger_reason: str
    seq_no: int
    transaction_data: Dict
    meter_value: List = None
    offline: bool = None
    number_of_phases_used: int = None
    cable_max_current: int = None
    reservation_id: int = None
    evse: Dict = None
    id_token: Dict = None


@dataclass
class TriggerMessagePayload:
    requested_message: str
    evse: Dict = None


@dataclass
class UnlockConnectorPayload:
    evse_id: int
    connector_id: int


@dataclass
class UnpublishFirmwarePayload:
    checksum: str


@dataclass
class Update15118EVCertificatePayload:
    _15118_schema_version: str
    exi_request: str


@dataclass
class UpdateFirmwarePayload:
    request_id: int
    firmware: Dict
    retries: int = None
    retry_interval: int = None
