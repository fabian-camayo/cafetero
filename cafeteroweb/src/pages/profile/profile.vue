<template >
    <section class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6">
                    <h1>Perfil</h1>
                </div>
            </div>
        </div>
        <!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-3">
                    <!-- Profile Image -->
                    <div class="card card-primary card-outline">
                        <div class="card-body box-profile">
                            <div class="text-center">
                                <img
                                    class="
                                        profile-user-img
                                        img-fluid img-circle
                                    "
                                    src="../../assets/img/default-profile.png"
                                    alt="User profile picture"
                                />
                            </div>

                            <h3 class="profile-username text-center">
                                {{ user.username }}
                            </h3>

                            <p class="text-muted text-center">
                                Usuario Proveedor
                            </p>
                        </div>
                        <!-- /.card-body -->
                    </div>
                    <!-- /.card -->
                </div>
                <!-- /.col -->
                <div class="col-md-9">
                    <div class="card">
                        <div class="card-header p-2">
                            <ul class="nav nav-pills"></ul>
                        </div>
                        <!-- /.card-header -->
                        <div class="card-body">
                            <div class="tab-content">
                                <form class="form-horizontal">
                                    <div class="form-group row">
                                        <label
                                            for="inputEmail"
                                            class="col-sm-2 col-form-label"
                                            >Correo</label
                                        >
                                        <div class="col-sm-10">
                                            <input
                                                v-model="user.username"
                                                disabled
                                                type="email"
                                                class="form-control"
                                                id="inputEmail"
                                                placeholder="Correo Electronico"
                                            />
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <label
                                            for="inputName2"
                                            class="col-sm-2 col-form-label"
                                            >Contraseña</label
                                        >
                                        <div class="col-sm-10">
                                            <input
                                                v-model="user.password"
                                                type="text"
                                                class="form-control"
                                                id="inputName2"
                                                placeholder="Cambiar Contraseña"
                                            />
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <div class="offset-sm-2 col-sm-10">
                                            <div class="checkbox">
                                                <label>
                                                    <input type="checkbox" />
                                                    Acepto los
                                                    <a href="#"
                                                        >terminos y
                                                        condiciones</a
                                                    >
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <div class="offset-sm-2 col-sm-10">
                                            <button
                                                @click="saveUser"
                                                type="submit"
                                                class="btn btn-danger"
                                            >
                                                Actualizar
                                            </button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <!-- /.tab-content -->
                        </div>
                        <!-- /.card-body -->
                    </div>
                    <!-- /.card -->
                </div>
                <!-- /.col -->
            </div>
            <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
    </section>
</template>
<script lang="ts">
import {defineComponent} from 'vue';
import UserDataService from '@/services/UserDataService';
import User from '@/types/User';
import ResponseData from '@/types/ResponseData';
import store from '@/store/index';
import jwt_decode from 'jwt-decode';

export default defineComponent({
    name: 'profile',
    data() {
        return {
            user: {
                id: null,
                username: '',
                password: ''
            } as User,
            submitted: false
        };
    },
    methods: {
        saveUser() {
            let data = {
                id: this.user.id,
                username: this.user.username,
                password: this.user.password
            };
            UserDataService.update(data.id, data)
                .then((response: ResponseData) => {
                    this.user.id = response.data.id;
                    this.submitted = true;
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        },
        newBatch() {
            this.submitted = false;
            this.user = {} as User;
        }
    },
    created() {
        let decoded: User = jwt_decode(store.getters.token);
        this.user.username = decoded.username;
        this.user.id = decoded.user_id;
    }
});
</script>
<style lang="scss"></style>