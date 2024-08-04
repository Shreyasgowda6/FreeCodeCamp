import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestTimeSeriesVisualizer(unittest.TestCase):

    def test_line_plot(self):
        draw_line_plot()  # Check if no error occurs during execution

    def test_bar_plot(self):
        draw_bar_plot()  # Check if no error occurs during execution

    def test_box_plot(self):
        draw_box_plot()  # Check if no error occurs during execution

if __name__ == '__main__':
    unittest.main()
