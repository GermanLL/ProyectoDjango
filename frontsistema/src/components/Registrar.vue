<template>
  <section Style="background-image:url(assets/img/gallery/bg.png)">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-6 col-lg-5 col-xl-4"><img src="assets/img/illustrations/callback.png" alt="" />
          <h5 class="text-danger">A SOLO UN CLICK</h5>
          <h2>Puedes resgistrate</h2>
          <p class="fs-1 mb-5"> Horario de atencion, Lunes a Viernes, 9 AM - 5 PM.</p>
        </div>
        <div class="col-md-6 col-lg-5 col-xl-4">
          <form class="row">
            <div>
              <div class="form-group" @submit.prevent="registrar">
                <label><b>Nombre:</b></label>
                <input type="text" class="form-control" required v-model="username" placeholder="Username" />
                <label><b>Password:</b></label>
                <input type="password" class="form-control" required v-model="password" placeholder="Password" />
                <label><b>Email:</b></label>
                <input type="text" class="form-control" required v-model="email" placeholder="Email" />
                <div class="text-center fs-6 fs-xxl-7">
                  <button class="btn btn-outline-danger" type="submit">Registrarme</button>
                </div>
              </div>
            </div>
          </form>
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
  name: "Registrar",
  data() {
    return {
      username: "",
      password: "",
      email: ""
    }
  },
  ///////
  methods: {
    registrar() {
      axios({
        url: "http://127.0.0.1:8000/auth/users/",
        data: {
          username: this.username,
          email: this.email,
          password: this.password
        },
        method: "POST"
      }).then((response) => {
        console.log(response.data);
        this.$router.push("/")
      });
    },
  },
  mounted() {
    //
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
