from django.urls import path
from .views import *

urlpatterns = [
    path('send-request/', SendRequest.as_view(), name="send_request"),
    path('cancel-request/<int:id>/', CancelRequest.as_view(), name="cancel_request"),
    path('requests-list/', OfficeSendRequestList.as_view(), name="requests_list"),
    path('receipt-print/<int:id>/', PrintReceipt.as_view(), name="receipt_print"),
    path('transactions/', GetOwnTransactions.as_view(), name="transactions"),
    path('transactions/<int:id>/', GetAgentTransactions.as_view(), name="agent_transactions"),
    path('transactions-dashboard/', GetFullTransactions.as_view(), name="transactions-dashboard"),
]