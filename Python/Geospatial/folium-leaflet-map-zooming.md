# Prevent Folium/Leaflet maps from zooming when you scroll past

As you scroll through a notebook, Folium/Leaflet maps tend to automatically zoom in/out and this stops you from scrolling easily through the notebook.

## Workaround

Scroll only on one edge of the notebook, so that your cursor does not get caught within the map as it scrolls by.

## UI adjustment via code

Or, you can disable zooming on scroll, and revert to using just the zoom in/out buttons, and double-clicking. To do this, I place the following code in a `utils.py`, then import and call the function at the top of each notebook. This means you can continue calling e.g. `gdf.explore()` and you don't pollute your code with UI adjustments.

```python
import folium
import matplotlib.pyplot as plt

def set_plotting_defaults():
    """Set default settings for plotting. Call this at the top of a notebook."""

    # Increased figure size for matplotlib plots
    plt.rcParams['figure.figsize'] = (10, 7)

    # Prevent maps created using Folium (e.g. when using GeoPandas) from zooming
    # with the mouse wheel
    original_method = folium.Map.__init__
    def replacement_method(*args, **kwargs):
        kwargs = {
            'scroll_wheel_zoom': False,
            **kwargs,
        }
        return original_method(*args, **kwargs)
    folium.Map.__init__ = replacement_method
```
