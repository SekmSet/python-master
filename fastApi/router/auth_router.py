from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)


@router.post("/signin")
async def signin():
    pass


@router.post("/login")
async def login():
    pass


@router.post("/logout")
async def logout():
    pass


@router.post("/delete")
async def delete():
    pass
