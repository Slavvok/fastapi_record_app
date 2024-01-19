from fastapi import APIRouter, HTTPException

from utils import save_record, fetch_record, fetch_record_list

router = APIRouter()


@router.post("/")
def add_record(data: str):
    try:
        record = save_record(data)
        if record:
            return record
        raise HTTPException(
            400,
            "Couldn't add a record."
        )
    except Exception:
        raise HTTPException(
            400,
            "Unable to get record"
        )


@router.get("/{number}")
def get_record(number):
    try:
        record = fetch_record(number)
        if record:
            return record
    except Exception:
        raise HTTPException(
            400,
            "Unable to get record"
        )


@router.get("/")
def get_record_list(f: int, l: int):
    try:
        if l < f:
            raise HTTPException(
                422, "Last can't be smaller than first."
            )
        record_list = fetch_record_list(f, l)
        if record_list:
            return record_list
        raise HTTPException(
            400,
            f"No records in range {f}, {l}"
        )
    except Exception:
        raise HTTPException(
            400,
            "Unable to get record list"
        )
