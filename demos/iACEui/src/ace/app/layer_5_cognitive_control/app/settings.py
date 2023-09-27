from base.settings import Settings


settings = Settings(
    role_name="layer_5_controller",
    send_hello=False,
    northbound_subscribe_queue="northbound.layer_5_controller",
    southbound_subscribe_queue="southbound.layer_5_controller",
    southbound_publish_queue="southbound.layer_6_prosecutor",
    northbound_publish_queue="northbound.layer_4_executive",
)