# Sparclet
A python library to generate and interact with flatmaps in a jupyter notebook using the ipyleaflet library. 

![alt text](https://github.com/SPARC-FAIR-Codeathon/Sparclet/blob/main/LeafLet%20AddOn%20Tutorial/Landing_page.png)



## Project Goals

SPARC has a large repository of datasets and interactive exploration applicaions like the SPARC flatmaps built into their portal. Although, the maps present high resolution intricate anatomical models across species, they are limited by static maps and corresponding literature & dataset retrieveal. In the codeathon, we aimed to add additional fucntionalities and further interactions with these maps. These additonal fucntionalities could help a researcher agument the research process and help in developing a deeper understanding of theor field of study. We added techniques to view the flatmaps in a jupyter notebook along with added widgets using the ipyleaflet library. We achieved this by building a new python library called Sparclet to aid us in this project. 


## Solution

We created Sparclet, a pypi application that allows flatmaps to be viewed in (Jupyter Notebook)[https://jupyter.org/] and be interacted in nivel ways using the (ipyleaflet library)[https://github.com/jupyter-widgets/ipyleaflet] to help facilitate an individualized research process. We went about this using the following solutions.
1. Simplified the process of retrieving flatmaps from their APIs by building a python routine that requires a user to only provide the model number of a species or a model to generate the maps locally. 
2. Added functions pertaining to adding markers and annotations that could be stored as study-specific file on a server.  
3. Added multiple functionalities such as layer control, hovering annotations, custom drawing tools, heatmaps and antpaths for interacting with the flatmaps
4. We also attempted to provide additonal fucntionalities such as comparing cross species maps with a splitmap feature with respect to specific anatomical regions. A search bar that could be used for navigating annotations and obtain methods used in relevant studies. 
5. Created a new open source python library that coule be used by the SPARC community in the future. The additional fucntionalities mentioned above will be the subjects of open source contributions to our library.


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
  

