from fastapi import APIRouter

router = APIRouter()


@router.get("/unlimited")
async def unlimited_requests():
    return {"message": "Unlimited requests available!"}


@router.get("/limited")
async def limited_requests():
    return {"message": "Limited requests, don't overuse!"}
