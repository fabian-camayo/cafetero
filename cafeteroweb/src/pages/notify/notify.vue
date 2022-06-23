<template >
    <section class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6">
                    <h1>Notificación SMS</h1>
                </div>
            </div>
        </div>
        <!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
        <div class="container-fluid">
            <div class="row">
                <!-- /.col -->
                <div class="col-md-12 pr-5 pl-5">
                    <div class="card p-3">
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
                                            >Número</label
                                        >
                                        <div class="col-sm-10">
                                            <input
                                                type="text"
                                                class="form-control"
                                                id="contact"
                                                v-model="notify.contact"
                                                placeholder="Ingrese el número de celular +573200000000"
                                            />
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <label
                                            for="inputExperience"
                                            class="col-sm-2 col-form-label"
                                            >Mensaje</label
                                        >
                                        <div class="col-sm-10">
                                            <textarea
                                                required
                                                class="form-control"
                                                id="inputExperience"
                                                v-model="notify.message"
                                                placeholder="Ingrese el contenido del mensaje"
                                            ></textarea>
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
                                                type="submit"
                                                class="btn btn-danger"
                                                @click="send"
                                            >
                                                Enviar SMS
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
import NotifyDataService from '@/services/NotifyDataService';
import Notify from '@/types/Notify';
import ResponseData from '@/types/ResponseData';
import {useToast} from 'vue-toastification';

let toast = useToast();
export default defineComponent({
    name: 'notify',
    data() {
        return {
            notify: {
                contact: '',
                message: ''
            } as Notify,
            submitted: false
        };
    },
    methods: {
        send() {
            let data = {
                contact: this.notify.contact,
                message: this.notify.message
            };
            NotifyDataService.send(data)
                .then((response: ResponseData) => {
                    console.log(response.data);
                    this.submitted = true;
                    toast.success('La Notificación fue enviada');
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        },
        newBatch() {
            this.submitted = false;
            this.notify = {} as Notify;
        }
    }
});
</script>
<style lang="scss"></style>