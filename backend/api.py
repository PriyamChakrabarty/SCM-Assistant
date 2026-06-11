from fastapi import FastAPI

from backend.rag_service import (
    SupplierAnalyticsService,
)

from backend.utils import (
    success_response,
    error_response,
)

app = FastAPI(
    title="SCM Assistant API",
    version="1.0.0",
)


@app.get("/")
def health():

    return {
        "status": "running"
    }


@app.get("/rebate")
def rebate():

    try:

        result = (
            SupplierAnalyticsService
            .rebate_suppliers()
        )

        return success_response(result)

    except Exception as e:

        return error_response(str(e))


@app.get("/swl")
def swl():

    try:

        result = (
            SupplierAnalyticsService
            .swl_suppliers()
        )

        return success_response(result)

    except Exception as e:

        return error_response(str(e))


@app.get("/disruptions")
def disruptions():

    try:

        result = (
            SupplierAnalyticsService
            .disruption_suppliers()
        )

        return success_response(result)

    except Exception as e:

        return error_response(str(e))


@app.get("/regional-spend")
def regional_spend():

    try:

        result = (
            SupplierAnalyticsService
            .regional_spend()
        )

        return success_response(result)

    except Exception as e:

        return error_response(str(e))


@app.get("/defects")
def defects():

    try:

        result = (
            SupplierAnalyticsService
            .defect_category()
        )

        return success_response(result)

    except Exception as e:

        return error_response(str(e))