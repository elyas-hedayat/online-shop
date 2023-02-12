from datetime import datetime

from zeep import Client

terminal_id = "3621439"
username = "p338"
password = "71973830"
url = "https://bpm.shaparak.ir/pgwchannel/services/pgw?wsdl"


def create_request(
    order_id: int,
    amount: int,
    payer_id: int,
    additional_data: str = None,
    mobile_number: str = "",
    callback_url=None,
):
    local_time = datetime.now().strftime("%H%M%S")
    local_date = datetime.now().strftime("%Y%m%d")
    client = Client(url)
    result = client.service.bpPayRequest(
        terminalId=terminal_id,
        userName=username,
        userPassword=password,
        callBackUrl=callback_url,
        payerId=payer_id,
        localDate=local_date,
        localTime=local_time,
        additionalData=str(additional_data),
        orderId=order_id,
        amount=10 * amount,
        mobileNo=mobile_number,
    )
    return result


def verify_request(order_id: int, sale_order_id: int, sale_reference_id: int):
    client = Client("https://bpm.shaparak.ir/pgwchannel/services/pgw?wsdl")
    result = client.service.bpVerifyRequest(
        terminalId=terminal_id,
        userName=username,
        userPassword=password,
        orderId=str(order_id),
        saleOrderId=str(sale_order_id),
        saleReferenceId=str(sale_reference_id),
    )
    return result
