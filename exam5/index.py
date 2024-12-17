from app.controllers.pages import PagesController
from http_fw.server import run
from http_fw.router import Router


router = Router()
router.get('/', PagesController, 'home')
router.get('/about', PagesController, 'about')
router.get('/new', PagesController, 'create_car_post')
router.post('/', PagesController, 'create_car_post')
router.get('/car', PagesController, 'get_car')

run(router)
