
import vsg_gui
from PyQt4 import QtGui, Qt
from gnuradio.filter import firdes
import sip
import numpy
import sys
import time

from gnuradio import qtgui, digital, blocks
from gnuradio import gr

# We always want these, so make them ahead of time
time_sink = qtgui.time_sink_c(1024, 32e3, "", 1)
freq_sink = qtgui.freq_sink_c(1024, firdes.WIN_BLACKMAN_hARRIS, 0, 32e3, "", 1)
# TODO: use fosphor sink instead of freq sink if it exists

# Make a dumb flowgraph for now
def make_psk_gen():
    tb = gr.top_block("Simple PSK Gen")
    psk_mod = digital.psk.psk_mod(constellation_points=8,
            mod_code="gray",
            differential=True,
            samples_per_symbol=2,
            excess_bw=0.35,
            verbose=False,
            log=False,
            )
    src = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 1000)), True)
    tb.connect((src, 0), (psk_mod, 0))
    tb.connect((psk_mod, 0), (time_sink, 0))
    return tb


# Create the application and set up view created from QtCreator
qapp = QtGui.QApplication(sys.argv)
win = QtGui.QMainWindow()
vsg = vsg_gui.Ui_MainWindow()
vsg.setupUi(win)

# Add the time sink to the view
time_sink_win = sip.wrapinstance(time_sink.pyqwidget(), Qt.QWidget)
time_layout = QtGui.QFormLayout()
time_layout.addWidget(time_sink_win)
vsg.timeDomainFrame.setLayout(time_layout)

# Add the frequency sink to the view
freq_sink_win = sip.wrapinstance(freq_sink.pyqwidget(), Qt.QWidget)
freq_layout = QtGui.QFormLayout()
freq_layout.addWidget(freq_sink_win)
vsg.freqDomainFrame.setLayout(freq_layout)

# Let's kick it off
win.show()

sys.exit(qapp.exec_())
