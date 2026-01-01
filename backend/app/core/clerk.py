from clerk_backeend_api import Clerk 
from app.core.config import settings

clerk = Clerk(bearer_auth=settings.CLERK_SECRET_KEY)