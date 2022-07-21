<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    <v-spacer></v-spacer>
      <div class="d-flex align-center">
        a search engine for interactive webbased visualizations
      </div>

      <v-spacer></v-spacer>

    </v-app-bar>

    <v-main>
      <SearchEngine/>
    </v-main>
  </v-app>
</template>

<script>
import SearchEngine from './components/SearchEngine';

export default {
  name: 'App',

  components: {
    SearchEngine
  },

  data: () => ({
    //
  }),
};
</script>
