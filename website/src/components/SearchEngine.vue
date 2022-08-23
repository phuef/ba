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
        <v-row>
            <v-list :key=item.url v-for="item in items"> 
            <v-col cols=12>
                <v-card v-if="isInFilter(item.type)" 
                        class="ma-auto my-12"
                        max-width="350"
                        d-flex flex-column flex
                >                     
                    <v-col >
                        <v-img
                            contain    
                            max-height="300"
                            min-height="100"
                            max-width="300"
                            min-width="100"
                            :src="screenshotLink(item.screenshot)"
                        ></v-img>
                    </v-col>
                    <v-col >
                        <v-card-title :href="item.url" target="_blank"> 
                            <a
                                :href="item.url"
                                class="text-decoration-none"
                                >{{getTitle(item.microlink)}}</a> 
                        </v-card-title>
                        <v-card-subtitle>
                            {{getDescription(item.microlink)}}
                        </v-card-subtitle>
                            <v-card-text>
                                <v-chip-group column=True>
                                <v-chip v-for="topic in item.topics" :key="topic" @click="chipSelected(topic)">{{topic}}</v-chip>
                            </v-chip-group>
                        </v-card-text>
                        
                    </v-col>
                </v-card>
            </v-col >
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
        chipSelected(topic){
            this.currentSearchQuery=topic
            this.getSearchResults()
            },
        screenshotLink(string){
            return "http://localhost:5000/img" +"?img=" +string
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
<style>
.v-list {
    display: block;
    padding: 2px 0;}
</style>