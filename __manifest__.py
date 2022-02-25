# -*- coding: utf-8 -*-
{
    'name': "Taftech",

    'sequence': 1,

    'description': """
        gestion et le suivi des hotels de taf_tech informatique
    """,

    'author': "Melax_dev",
    'website': "https://gitlab.melaximport.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','commerciale'],

    # always loaded
    'data': [
            'views/chambre.xml',
            'views/service.xml',
            'views/clientH.xml',
            'views/personnelH.xml',
            'views/paiementH.xml',
            'views/reservation.xml',
            'views/facturation.xml',
            'views/specification.xml',
            'views/clientResto.xml',
            'views/commandeResto.xml',
            'views/factureResto.xml',
            'views/menuResto.xml',
            'views/personnelResto.xml',
            'views/produitResto.xml',
            'views/rapportmenuResto.xml',
            'views/clientFF.xml',
            'views/commandeFF.xml',
            'views/factureFF.xml',
            'views/menuFF.xml',
            'views/personnelFF.xml',
            'views/produitFF.xml',
            'views/rapportmenuFF.xml',
            'views/clientBar.xml',
            'views/commandeBar.xml',
            'views/factureBar.xml',
            'views/personnelBar.xml',
            'views/produitBar.xml',
            'menu/menu.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'auto_install': False,
    'application':True,
}
