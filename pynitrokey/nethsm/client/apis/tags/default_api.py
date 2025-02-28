# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from pynitrokey.nethsm.client.paths.keys_key_id_csr_pem.post.operation import KeysKeyIDCsrPemPost
from pynitrokey.nethsm.client.paths.system_factory_reset.post.operation import SystemFactoryResetPost
from pynitrokey.nethsm.client.paths.system_commit_update.post.operation import SystemCommitUpdatePost
from pynitrokey.nethsm.client.paths.system_update.post.operation import SystemUpdatePost
from pynitrokey.nethsm.client.paths.system_info.get.operation import SystemInfoGet
from pynitrokey.nethsm.client.paths.config_tls_csr_pem.post.operation import ConfigTlsCsrPemPost
from pynitrokey.nethsm.client.paths.config_tls_generate.post.operation import ConfigTlsGeneratePost
from pynitrokey.nethsm.client.paths.keys_key_id_decrypt.post.operation import KeysKeyIDDecryptPost
from pynitrokey.nethsm.client.paths.users_user_id_tags.get.operation import UsersUserIDTagsGet
from pynitrokey.nethsm.client.paths.config_tls_cert_pem.get.operation import ConfigTlsCertPemGet
from pynitrokey.nethsm.client.paths.config_tls_cert_pem.put.operation import ConfigTlsCertPemPut
from pynitrokey.nethsm.client.paths.system_backup.post.operation import SystemBackupPost
from pynitrokey.nethsm.client.paths.provision.post.operation import ProvisionPost
from pynitrokey.nethsm.client.paths.keys_key_id_sign.post.operation import KeysKeyIDSignPost
from pynitrokey.nethsm.client.paths.health_state.get.operation import HealthStateGet
from pynitrokey.nethsm.client.paths.keys_key_id_cert.delete.operation import KeysKeyIDCertDelete
from pynitrokey.nethsm.client.paths.keys_key_id_cert.get.operation import KeysKeyIDCertGet
from pynitrokey.nethsm.client.paths.keys_key_id_cert.put.operation import KeysKeyIDCertPut
from pynitrokey.nethsm.client.paths.keys_key_id_encrypt.post.operation import KeysKeyIDEncryptPost
from pynitrokey.nethsm.client.paths.system_cancel_update.post.operation import SystemCancelUpdatePost
from pynitrokey.nethsm.client.paths.keys_key_id_public_pem.get.operation import KeysKeyIDPublicPemGet
from pynitrokey.nethsm.client.paths.config_unlock_passphrase.put.operation import ConfigUnlockPassphrasePut
from pynitrokey.nethsm.client.paths.system_reboot.post.operation import SystemRebootPost
from pynitrokey.nethsm.client.paths.keys_key_id_restrictions_tags_tag.delete.operation import KeysKeyIDRestrictionsTagsTagDelete
from pynitrokey.nethsm.client.paths.keys_key_id_restrictions_tags_tag.put.operation import KeysKeyIDRestrictionsTagsTagPut
from pynitrokey.nethsm.client.paths.unlock.post.operation import UnlockPost
from pynitrokey.nethsm.client.paths.config_logging.get.operation import ConfigLoggingGet
from pynitrokey.nethsm.client.paths.config_logging.put.operation import ConfigLoggingPut
from pynitrokey.nethsm.client.paths.lock.post.operation import LockPost
from pynitrokey.nethsm.client.paths.config_unattended_boot.get.operation import ConfigUnattendedBootGet
from pynitrokey.nethsm.client.paths.config_unattended_boot.put.operation import ConfigUnattendedBootPut
from pynitrokey.nethsm.client.paths.keys_generate.post.operation import KeysGeneratePost
from pynitrokey.nethsm.client.paths.config_tls_public_pem.get.operation import ConfigTlsPublicPemGet
from pynitrokey.nethsm.client.paths.info.get.operation import InfoGet
from pynitrokey.nethsm.client.paths.config_backup_passphrase.put.operation import ConfigBackupPassphrasePut
from pynitrokey.nethsm.client.paths.health_ready.get.operation import HealthReadyGet
from pynitrokey.nethsm.client.paths.config_time.get.operation import ConfigTimeGet
from pynitrokey.nethsm.client.paths.config_time.put.operation import ConfigTimePut
from pynitrokey.nethsm.client.paths.system_shutdown.post.operation import SystemShutdownPost
from pynitrokey.nethsm.client.paths.config_network.get.operation import ConfigNetworkGet
from pynitrokey.nethsm.client.paths.config_network.put.operation import ConfigNetworkPut
from pynitrokey.nethsm.client.paths.keys_key_id.delete.operation import KeysKeyIDDelete
from pynitrokey.nethsm.client.paths.keys_key_id.get.operation import KeysKeyIDGet
from pynitrokey.nethsm.client.paths.keys_key_id.put.operation import KeysKeyIDPut
from pynitrokey.nethsm.client.paths.health_alive.get.operation import HealthAliveGet
from pynitrokey.nethsm.client.paths.metrics.get.operation import MetricsGet
from pynitrokey.nethsm.client.paths.users_user_id_passphrase.post.operation import UsersUserIDPassphrasePost
from pynitrokey.nethsm.client.paths.users_user_id.delete.operation import UsersUserIDDelete
from pynitrokey.nethsm.client.paths.users_user_id.get.operation import UsersUserIDGet
from pynitrokey.nethsm.client.paths.users_user_id.put.operation import UsersUserIDPut
from pynitrokey.nethsm.client.paths.system_restore.post.operation import SystemRestorePost
from pynitrokey.nethsm.client.paths.users_user_id_tags_tag.delete.operation import UsersUserIDTagsTagDelete
from pynitrokey.nethsm.client.paths.users_user_id_tags_tag.put.operation import UsersUserIDTagsTagPut
from pynitrokey.nethsm.client.paths.keys.get.operation import KeysGet
from pynitrokey.nethsm.client.paths.keys.post.operation import KeysPost
from pynitrokey.nethsm.client.paths.random.post.operation import RandomPost
from pynitrokey.nethsm.client.paths.users.get.operation import UsersGet
from pynitrokey.nethsm.client.paths.users.post.operation import UsersPost


class DefaultApi(
    KeysKeyIDCsrPemPost,
    SystemFactoryResetPost,
    SystemCommitUpdatePost,
    SystemUpdatePost,
    SystemInfoGet,
    ConfigTlsCsrPemPost,
    ConfigTlsGeneratePost,
    KeysKeyIDDecryptPost,
    UsersUserIDTagsGet,
    ConfigTlsCertPemGet,
    ConfigTlsCertPemPut,
    SystemBackupPost,
    ProvisionPost,
    KeysKeyIDSignPost,
    HealthStateGet,
    KeysKeyIDCertDelete,
    KeysKeyIDCertGet,
    KeysKeyIDCertPut,
    KeysKeyIDEncryptPost,
    SystemCancelUpdatePost,
    KeysKeyIDPublicPemGet,
    ConfigUnlockPassphrasePut,
    SystemRebootPost,
    KeysKeyIDRestrictionsTagsTagDelete,
    KeysKeyIDRestrictionsTagsTagPut,
    UnlockPost,
    ConfigLoggingGet,
    ConfigLoggingPut,
    LockPost,
    ConfigUnattendedBootGet,
    ConfigUnattendedBootPut,
    KeysGeneratePost,
    ConfigTlsPublicPemGet,
    InfoGet,
    ConfigBackupPassphrasePut,
    HealthReadyGet,
    ConfigTimeGet,
    ConfigTimePut,
    SystemShutdownPost,
    ConfigNetworkGet,
    ConfigNetworkPut,
    KeysKeyIDDelete,
    KeysKeyIDGet,
    KeysKeyIDPut,
    HealthAliveGet,
    MetricsGet,
    UsersUserIDPassphrasePost,
    UsersUserIDDelete,
    UsersUserIDGet,
    UsersUserIDPut,
    SystemRestorePost,
    UsersUserIDTagsTagDelete,
    UsersUserIDTagsTagPut,
    KeysGet,
    KeysPost,
    RandomPost,
    UsersGet,
    UsersPost,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    pass
