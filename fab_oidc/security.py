from flask_appbuilder.security.manager import AUTH_OID
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_oidc import OpenIDConnect
from airflow.www.security import AirflowSecurityManager
from .views import AuthOIDCView
from logging import getLogger
log = getLogger(__name__)


class OIDCSecurityManagerMixin:

    def __init__(self, appbuilder):
        super().__init__(appbuilder)
        if self.auth_type == AUTH_OID:
            self.oid = OpenIDConnect(self.appbuilder.get_app)
            self.authoidview = AuthOIDCView


class OIDCSecurityManager(OIDCSecurityManagerMixin, SecurityManager):
    pass



class AirflowOIDCSecurityManager(OIDCSecurityManagerMixin,
                                 AirflowSecurityManager):
    pass