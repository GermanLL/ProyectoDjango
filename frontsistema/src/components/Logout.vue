<template>
    <div>
        <h1 class="display-1 text-center">Logout</h1>
    </div>
    </template>
    
    <script>
    import axios from "axios"
    export default {
        //////
      // eslint-disable-next-line vue/multi-word-component-names
      name: 'Logout',
      data() {
          return {
              username: "",
              password: "",
          };
      },
      ///////
      methods: {
          logout() {
            axios({
                  url: 'http://127.0.0.1:8000/auth/token/logout/',
                  headers : {Authorization : "Token " + this.$store.getters.getToken},
                  method: 'POST'
            }).then((response) => {
                this.$store.commit('unLogUser');
                console.log(response.data);
                this.$router.push('/');
            });
          },
      },
      mounted() {
          this.logout();
          //
      },
    };
    </script>
  

<!-- Add "scoped" attribute to limit CSS to this component only -->
