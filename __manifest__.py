{
    "name": "MLR ecommerce BTCpay",
    "summary": "MLR ecommerce BTCpay",
    "author": "ERP",
    "website": "https://www.milightningrod.com",
    "category": "Ecommerce",
    "version": "1.0",
    "depends": ["website"],
    "data": [
        "data/btcpay_payment_provider_data.xml",
        "data/btcpay_payment_icons.xml",
        "views/btcpay_payment_provider.xml",
        "views/btcpay_payment_template.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    "license": "OPL-1",
}
