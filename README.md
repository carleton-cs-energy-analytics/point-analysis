# Point-Analysis
Collection of scripts used to investigate and decode point names as well as eventually import the information that was decoded to the database.
This process should only be done when point descriptions have changed, or decoding scripts have changed.
##  Updating due to Changed Point Definitions
This should be very infrequent, only occurring when renovations or new construction occurs.
In this case, we need to update points.json. 
1.  Update definition files in siemens-point-descriptions with the new definitions
2. run `python3 analysis-tools/definitions2json.py`


## Importing Points to DB
Every time the decoders are updated, the importer needs to be run again. 
1. from the backend repo, run the `drop.sql`, `schema.sql`, and `seed.sql` scripts in the `migrations` directory (in that order). 
2. run `python3 importers/importer.py`

Note: if importing to the production DB, the `DATABASE_HOST`, `DATABASE_NAME`, `DATABASE_USER`, and `DATABASE_PASSWORD`
environment variables will have to be set. If not set, it defaults to the local database.

## Project Structure & Making Decoder Changes
#### siemens_master
This script contains the master decoding function which reads info from `points.json`, 
and creates point objects using the correct decoder for each point. This function is called
from the importer.

#### Decoders
all of the `*point_decoder.py` files contain classes that are collections of static methods that
decode different aspects of a point. They all inherit from `point_decoder.py`, which acts as a 
general decoder for things that are consistent across buildings. Right now, we have a decoder for each 
building, and one "override_point_decoder" for points we want to decode seperate from their building. This
hierarchy could be extended one level deeper if we find out that, for example, in some building there are two 
general trends for decoding certain atrributes of a point. 

### Importer 
The script that gets decoded point objects from siemens_master, and imports them to the database.

### Tests
These are not true unit tests. They don't tests specific methods. Instead, they are more like end-to-end tests of 
the entire decoding process. They run the decoders, then test that all the points conform to 
things that should be true. For example, "all points have a point name" etc.