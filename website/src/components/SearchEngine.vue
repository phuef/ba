<template>
    <v-container>
        <!-- search field-->
        <v-card>
            <!-- search bar -->
            <v-text-field
                v-model="currentSearchQuery"
                ref="search"
                full-width
                hide-details
                label="Search"
                single-line
                solo
                placeholder="type in your search query"
                append-icon="mdi-magnify"
                @keyup.enter="getSearchResults(currentSearchQuery)"
          ></v-text-field>
          <v-card-text v-if="searchText">
              {{searchText}}
          </v-card-text>
        </v-card>
        <v-divider></v-divider>
        <!-- filter options -->
        <!--<v-list>
                <v-row>                    
                    <v-spacer></v-spacer>
                <v-checkbox
                    v-model="filter"
                    dense
                    label="interactive visualizations (IV / IGV)"
                    value="IV"
                ></v-checkbox>
                <v-spacer></v-spacer>
                <v-checkbox
                    v-model="filter"
                    dense
                    input-value
                    label="interactive geo visualizations (IGV)"
                    value="IGV"
                ></v-checkbox>
                <v-spacer></v-spacer>
                <v-checkbox
                    v-model="filter"
                    dense
                    label="no interactive visualizations (noIV)"
                    value="noIV"
                ></v-checkbox>
                <v-spacer></v-spacer>

                </v-row>
        </v-list>-->
        <!-- search results -->
        <v-row>
            <v-list :key=item.url v-for="item in items" class="pa-4"> 
            <v-card v-if="isInFilter(item.type)" > <!--:color="getColor(item.type)"-->
            <!-- ({{item.type}}) -->
                <v-card-title> 
                    {{getTitle(item.microlink)}} 
                </v-card-title>
                <v-card-subtitle>
                    {{getDescription(item.microlink)}}
                </v-card-subtitle>
                <v-card-text>
                    <a
                        :href="item.url"
                        class="text-decoration-none"
                        >{{item.url}}</a>
                    
                </v-card-text>
                <v-card-text>
                    {{beautifyTopics(item.topics)}}
                </v-card-text>
                <v-divider></v-divider>

            </v-card>
            </v-list>
        </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'SearchEngine',
    data: () => ({
         
                searchResults:[],
                items:[],
                filter: null,
                searchText: undefined,
                currentSearchQuery: undefined,

            
    }),
    methods:{
        // GETs the search results from the API
        getSearchResults(){

            //API call
            fetch("http://localhost:5000/search"
            +"?search_query="+this.currentSearchQuery, {
                "method": "GET",
                "headers": {
                }
                })
                .then((response) => response.json())
                .then((responseJSON) => {
                    // do stuff with responseJSON
                    this.items=this.transformSearchResults(this.searchResults=responseJSON);
                    console.log(this.items);

                    // text to show the found results
                    var temp=typeof this.currentSearchQuery!=="undefined"&&this.currentSearchQuery!=="" ? " for " +this.currentSearchQuery: "";
                    this.searchText="the search" +temp  +" got " +this.items.length + (this.items.length===1?" result":" results")
                })
            .catch(err => {
                console.error(err);
            })
           },

        // transforms the search results to a json
        transformSearchResults(results){
            //returns the transformed search results
            return(JSON.parse(JSON.stringify(results)))

        },

        // checks whether a filter exists and if the given type is included in the filter
       isInFilter(type){
           console.log(type)
           return true
            /*if(this.filter===null){ //does a filter exist
                return true
            }
            else if (type===this.filter){ //is the type equal to the filter
                return true //ToDO: enable multiple filters --> IV and noIV is a possibility
            }
            else if (type==="IGV" && this.filter==="IV"){
                return true
            }
            else {
                return false
            }*/
        },

        // returns the title that the microlink api returned
        getTitle(microlink){
            var micro=JSON.parse(JSON.stringify(microlink))
            return micro.data.title;
        },
        // returns the description that the microlink api returned
        getDescription(microlink){
            var micro=JSON.parse(JSON.stringify(microlink))
            return micro.data.description;
        },

        //returns a string with the topics in the following style: "Topics: topic1, topic2, ... topicN"
        beautifyTopics(topicsArray){
            var temp="Topics:";
            for (var i in topicsArray){
                temp='' +temp +' ' +topicsArray[i] +','
            }
            return temp.slice(0, temp.length -1)
        }
    }
    }
</script>