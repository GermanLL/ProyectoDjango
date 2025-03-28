<template>
  <section Style="background-image:url(assets/img/gallery/hero-header-bg.png)">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 ">
          <div class="card card-span rounded-5 mb-3">
            <div class="row" style="border-radius: 2rem;">
              <div class="col-md-6 col-lg-7 d-flex">
                <img class="w-100 fit-cover rounded-md-start rounded-top rounded-md-top-0"
                  src="assets/img/gallery/map.svg" alt="map" />
              </div>
              <div class="col-md-6 col-lg-5 d-flex flex-center">
                <div>
                  <h1 class="fw-normal text-center fs-6 fs-xxl-7 ">
                    Iniciar sesión</h1>
                  <h2>Ingrese sus datos</h2>
                  <div>
                    <form class="form-group" @submit.prevent="loguear">
                      <label><b>Nombre:</b></label>
                      <input type="text" class="form-control" required v-model="username" placeholder="Username">
                      <label><b>Password:</b></label>
                      <input type="password" class="form-control" required v-model="password" placeholder="Password">

                      <div class="text-center fs-6 fs-xxl-7">
                        <button class="btn btn-outline-danger" type="submit">Loguearme</button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import axios from "axios";
export default {
  //////
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  ///////
  methods: {
    loguear() {
      axios({
        url: "http://127.0.0.1:8000/auth/token/login/",
        data: { username: this.username, password: this.password },
        method: "POST",
      }).then((response) => {
        //console.log(response.data);
        this.$store.commit(
          "logUser",
          response.data.auth_token,
          response.data.id
        );
        this.$router.push("/");
      });
    },
  },
  mounted() {
    //
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
