from sparclet import *

def main():
    # Whole rat flatmap 
    map1 = Build_Map('https://mapcore-demo.org/current/flatmap/v2', 2)
    # Build given map
    built_map = map1.build_map_without_markers()
    # Leaflet addons
    leaf = leaflet_addons(map1, built_map)
    # Example addon: Hover over map to see label names
    leaf.hover()
    
if __name__ == '__main__':
    main()