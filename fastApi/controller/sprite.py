class SpriteController:

    async def get_sprites(self):
        return ({"message": "Get all sprites"})

    async def get_sprite_by_id(self, id: int):
        return ({"message": "Get one sprite by ID", "id": id})

    async def get_sprite_by_name(self, name: str):
        return ({"message": "Get one sprite by ID", "name": name})

    async def create_sprite(self):
        return ({"message": "Create a new sprite"})

    async def update_sprite(self, id: int):
        return ({"message": "Update sprite by ID", "id": id})

    async def delete_sprite(self, id: int):
        return ({"message": "Delete sprite by ID", "id": id})


sprite_controller = SpriteController()
