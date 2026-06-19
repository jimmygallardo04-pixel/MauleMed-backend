from rest_framework import serializers

from apps.accounts.serializers import UserSerializer
from apps.organizations.serializers import (
    LegalEntitySmallSerializer,
    BranchSmallSerializer,
    CostCenterSmallSerializer,
)
from apps.products.serializers import ProductCategorySmallSerializer
from apps.suppliers.serializers import SupplierSmallSerializer
from apps.purchasing.serializers import PurchaseOrderSmallSerializer

from .models import SupplierInvoice, Payment, Budget


class SupplierInvoiceSmallSerializer(serializers.ModelSerializer):
    supplier_detail = SupplierSmallSerializer(source="supplier", read_only=True)

    class Meta:
        model = SupplierInvoice
        fields = ["uuid", "invoice_number", "status", "total_amount", "supplier_detail"]


class SupplierInvoiceSerializer(serializers.ModelSerializer):
    supplier_detail = SupplierSmallSerializer(source="supplier", read_only=True)
    legal_entity_detail = LegalEntitySmallSerializer(source="legal_entity", read_only=True)
    branch_detail = BranchSmallSerializer(source="branch", read_only=True)
    cost_center_detail = CostCenterSmallSerializer(source="cost_center", read_only=True)
    purchase_order_detail = PurchaseOrderSmallSerializer(source="purchase_order", read_only=True)

    class Meta:
        model = SupplierInvoice
        exclude = ["id", "deleted_at"]


class PaymentSerializer(serializers.ModelSerializer):
    supplier_invoice_detail = SupplierInvoiceSmallSerializer(source="supplier_invoice", read_only=True)
    legal_entity_detail = LegalEntitySmallSerializer(source="legal_entity", read_only=True)
    created_by_detail = UserSerializer(source="created_by", read_only=True)

    class Meta:
        model = Payment
        exclude = ["id", "deleted_at"]


class BudgetSerializer(serializers.ModelSerializer):
    legal_entity_detail = LegalEntitySmallSerializer(source="legal_entity", read_only=True)
    branch_detail = BranchSmallSerializer(source="branch", read_only=True)
    cost_center_detail = CostCenterSmallSerializer(source="cost_center", read_only=True)
    category_detail = ProductCategorySmallSerializer(source="category", read_only=True)

    available_amount = serializers.DecimalField(
        max_digits=14,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = Budget
        exclude = ["id", "deleted_at"]
