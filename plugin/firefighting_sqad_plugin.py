from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsProject
from .main import main

class FirefightingSquadPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = self.iface.pluginPath('firefighting_squad_plugin')
        self.action = None

    def initGui(self):
        self.action = QAction(QCoreApplication.translate("FirefightingSquadPlugin", "Run Firefighting Mission"), self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("Firefighting Squad Plugin", self.action)

    def unload(self):
        if self.action:
            self.iface.removePluginMenu("Firefighting Squad Plugin", self.action)
            self.iface.removeToolBarIcon(self.action)

    def run(self):
        # Ensure a QGIS project is loaded
        if not QgsProject.instance().fileName():
            QMessageBox.critical(self.iface.mainWindow(), "Error", "Please load a QGIS project before running the plugin.")
            return

        # Example usage with hardcoded drone connection strings, replace as needed
        try:
            main(num_wdd=3, num_wpd=3, wdd_conn_strings=['127.0.0.1:14550', '127.0.0.1:14551', '127.0.0.1:14552'],
                 wpd_conn_strings=['127.0.0.1:14553', '127.0.0.1:14554', '127.0.0.1:14555'])
            QMessageBox.information(self.iface.mainWindow(), "Success", "Firefighting mission completed successfully!")
        except Exception as e:
            QMessageBox.critical(self.iface.mainWindow(), "Error", f"An error occurred: {e}")
