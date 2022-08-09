__copyright__ = 'Copyright 2020, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'

from qgis.core import Qgis, QgsApplication, QgsMessageLog
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.utils import iface

from raepa.actions import (
    annuler_la_derniere_modification,
    calcul_orientation_appareil,
    couper_la_canalisation_sous_cet_ouvrage,
    inverser_canalisation,
    network_to_vanne,
    parcourir_reseau_depuis_cet_objet,
    parcourir_reseau_jusquaux_vannes,
    parcourir_reseau_jusquaux_vannes_fermees,
)
from raepa.dock import RaepaDock
from raepa.processing.provider import RaepaProvider


class Raepa:

    def __init__(self):
        self.provider = None
        self.dock = None

    def initProcessing(self):
        """Init Processing provider."""
        self.provider = RaepaProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        """Init the user interface."""
        self.initProcessing()
        self.dock = RaepaDock()
        iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)

    def unload(self):
        """Unload the plugin."""
        QgsApplication.processingRegistry().removeProvider(self.provider)
        iface.removeDockWidget(self.dock)
        self.dock.deleteLater()

    @staticmethod
    def run_action(name, *args):
        """Run a specific action.

        Do not rename this function, it's part of the public API of the plugin.

        These lines are included in the QGIS project.

        from qgis.utils import plugins
        plugins['raepa'].run_action('action_name', params)
        """
        # Dictionary of actions:
        # - number of arguments it expects
        # - function to call
        # - extra args to add on runtime
        actions = {
            'inverser_canalisation':
                [2, inverser_canalisation],
            'ouvrage_annuler_derniere_modification':
                [2, annuler_la_derniere_modification],
            'ouvrage_couper_canalisation_sous_cet_ouvrage':
                [2, couper_la_canalisation_sous_cet_ouvrage],
            'parcourir_reseau_depuis_cet_objet':
                [2, parcourir_reseau_depuis_cet_objet, 0],
            'parcourir_reseau_jusquaux_vannes':
                [2, parcourir_reseau_jusquaux_vannes],
            'parcourir_reseau_jusquaux_vannes_fermees':
                [2, parcourir_reseau_jusquaux_vannes_fermees],
            'calcul_orientation_appareil':
                [1, calcul_orientation_appareil],
            'network_to_vanne':
                [1, network_to_vanne]
        }
        if name not in actions:
            QMessageBox.critical(
                None, 'Action non trouvée', 'L\'action n\'a pas été trouvée.')
            return

        if actions[name][0] != len(args):
            QMessageBox.critical(
                None, 'Mauvais nombre d\'arguments', 'Mauvais nombre d\'arguments pour l\'action.')
            return

        params = list(args)
        if len(actions[name]) > 2:
            params += actions[name][2:]

        QgsMessageLog.logMessage(
            'Appel de l\'action {} avec les arguments: {}'.format(name, ', '.join(['{}'.format(i) for i in params])),
            'RAEPA', Qgis.Info)
        actions[name][1](*params)
