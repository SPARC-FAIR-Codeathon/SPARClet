# Sparclet
A python library to generate and interact with flatmaps in a jupyter notebook using the ipyleaflet library. 

![alt text](https://github.com/SPARC-FAIR-Codeathon/Sparclet/blob/main/LeafLet%20AddOn%20Tutorial/Landing_page.png)



## Project Goals

SPARC has a large data library with many flatmaps built off of data in their database. They have great detail,but there are limited action for the maps. We believed it would benefit a researcher if they could interact with the map. Leaflet is a software that uses javascript to interact with maps. TIOBE (The Importance Of Being Earnest) reports python is the most popular language. We thought using jupyter notebooks with python would be more accessible to researchers. We then found ipyleaflet, a python package that mimics leaflet.


## Solution

We created Sparclet, a pypi application that allows flatmaps to be viewed in (Jupyter Notebook)[https://jupyter.org/] and be used in new and different ways using (leaflet software)[https://leafletjs.com/index.html] to further understand the information shown in the flatmaps. The functions we created are:
1. Viewing two maps side by side in a split map. there are different approaches:
   - a chosen SPARC flatmap compared to another chosen SPARC flatmap
   - a chosen image or flatmap from an outside source compared with a SPARC flatmap
2. Apply annotations from metadata to flatmap i.e anatomical nomenclature
3. The ability to hover over map and get real time feedback
4. Markers on flatmap for defined anatomy
5. The ability to annotate the map by adding polygons, lines, or text

## Functions

Listed below are functions that can be called in regard to their class

### CustomWTKLayer class
    _get_data1: stores annotaion data in self.data
    
### Build_map class
    __init__: this is the function that calls the class itself. the parameters it takes in are the server url and the tag. The tag is the index in the list of image layers in the server. To determine the tag you will have to use a GET request like below
    
     import requests
     req = requests.get(server_url)
     url_dict = req.json()
     print(url_dict)
     
      then see where the desired flatmap falls in the dictionary, the index is the tag (remeber index starts at 0)
    
    get_url_dict: retrieves the Accept header, giving details on max zoom, min zoom, and bounds
    
    get_model_id: retrieves the unique id attached to the flatmap, used in the url
    
    get_model_name: retrieves the identifiable name for the flatmap
    
    get_model_layer_url: creates the url that is linked to the location of the layer in the server
    
    get_model_image_layer: retrieves image that make up the flatmap
    
    get_tile_urls: creates and returns tile urls that make up the map used in ipyleaflet
    
    get_annotations: retrieves annotation data that correlates with the flatmap features

    split_map: puts two maps side by side for analysis
    
    build_map_without_markers: creates the general flatmap with out feature markers
    
### leaflet_addons class
   
    add_markers: adds markers to the location of the annotation feature
   
    hover: allows the user to hover over the flatmap and get real time feedback
   
    update_html: updates the widget at bottom right with label of the current object being hovered on
   
## Sparclet python package
We welcome open source contributions to our library. There a many more functionalities that can be added to the flatmaps and we were restricted by the duration of the codeathon. We will be maintaining this library and making it more beneficial to the SPARC community. 

## Team Members

Archit Bhatnagar
-Max Planck Institute of Molecular Cell Biology and Genetics, Dresden

Chloe Hoff
-Undergrad at the University of Vermont

Koustubh Sudarshan
-Dalhousie University, Canada & UCLA Cardiac Arrhythmia Center, USA .
  

