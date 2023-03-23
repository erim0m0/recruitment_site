<template>
    <div class="Verify">
        <div class="Signup">
            <section class="ftco-section">
                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-md-6 col-lg-4">
                            <div class="login-wrap p-0">
                                <h3 class="mb-4 text-center"></h3>
                                <form @submit.prevent="doVerify" class="signin-form">
                                    <div class="form-group">
                                        <input v-model="code" dir="ltr" type="text" class="form-control" placeholder="Code"
                                            :class="{
                                                'is-valid': codeE === false,
                                                'is-invalid': codeE === true,
                                            }">
                                        <div class="invalid-feedback" v-if="codeE">
                                            {{ codeEM }}
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-primary">تایید</button>
                                </form>
                                <p class="w-100 text-center">&mdash; Or Sign In With &mdash;</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

export default {
    name: 'Verify',
    data() {
        return {
            code: "",
            codeE: null,
            codeEM: null,
        }
    },
    methods: {
        doVerify() {
            let access = true

            if (this.code === "") {
                access = false
                this.codeE = true
                this.codeEM = 'کد را وارد کنید.'
            } else {
                this.codeE = false
                this.codeEM = ''
            }

            if (access) {
                axios
                    .post('/account/api/verify/', {
                        "phone": localStorage.getItem("userPhone"),
                        "id_code": localStorage.getItem("id_code"),
                        "code": this.code
                    })
                    .then(response => {
                        localStorage.removeItem("id_code")
                        if (response.data.access) {
                            this.$store.commit("login", response.data)
                        }
                        this.$router.push("/")
                    })
                    .catch(error => {
                        this.codeE = true
                        if (error.response.status == 401) {
                            this.codeEM = "کد نامعتبر است."
                        }
                        console.log(error.response);
                    })
            }
        }
    },
}

</script>