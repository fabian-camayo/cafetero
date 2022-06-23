<template>
    <section class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6"></div>
                <div class="col-sm-6">
                    <ol class="breadcrumb float-sm-right">
                        <router-link to="/batch">
                            <button type="button" class="btn btn-default">
                                <li class="breadcrumb-item">
                                    Lotes de producción
                                </li>
                            </button>
                        </router-link>
                    </ol>
                </div>
            </div>
        </div>
        <!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="container-fluid pr-5 pl-5">
        <div class="card card-default pr-5 pl-5">
            <div class="card-header p-3 align-self-center">
                <h1 class="card-title">Ingrese un nuevo lote a la cosecha</h1>
            </div>
            <!-- /.card-header -->
            <!-- form start -->
            <form>
                <div class="card-body">
                    <div class="form-group">
                        <label for="code">Código</label>
                        <input
                            required
                            disabled
                            type="text"
                            class="form-control"
                            id="code"
                            v-model="batch.code"
                            placeholder="Ingrese un Código"
                        />
                    </div>
                    <div class="form-group">
                        <label for="weight">Nombre del Asociado</label>
                        <input
                            required
                            type="text"
                            class="form-control"
                            id="weight"
                            v-model="batch.contact_name"
                            placeholder="Ingrese el nombre del asociado"
                        />
                    </div>
                    <div class="form-group">
                        <label for="weight">Número de Celular Asociado</label>
                        <input
                            required
                            type="text"
                            class="form-control"
                            id="weight"
                            v-model="batch.contact"
                            placeholder="Ingrese el número de celular del asociado"
                        />
                    </div>
                    <div class="form-group">
                        <label for="weight">Peso (Kilogramos)</label>
                        <input
                            required
                            type="number"
                            class="form-control"
                            id="weight"
                            v-model="batch.weight"
                            placeholder="Ingrese el peso"
                        />
                    </div>
                    <div class="form-group">
                        <label for="coffe_type">Tipo de Cafe</label>
                        <select
                            required
                            name="coffe_type"
                            id="coffe_type"
                            class="form-control"
                            placeholder="Ingrese el tipo de cafe"
                            v-model="batch.coffe_type"
                        >
                            <option value="ARABIGO">ARABIGO</option>
                            <option value="ROBUSTA">ROBUSTA</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="varieties">Variedad</label>
                        <select
                            required
                            name="varieties"
                            id="varieties"
                            class="form-control"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="batch.varieties"
                            v-if="batch.coffe_type == 'ARABIGO'"
                        >
                            <option value="TIPICA">TIPICA</option>
                            <option value="BORBON">BORBON</option>
                            <option value="MARAGOGIPE">MARAGOGIPE</option>
                            <option value="TABI">TABI</option>
                            <option value="COLOMBIA">COLOMBIA</option>
                        </select>
                        <select
                            name="varieties"
                            id="varieties"
                            class="form-control"
                            placeholder="Ingrese la variedad del cafe"
                            v-model="batch.varieties"
                            v-if="batch.coffe_type == 'ROBUSTA'"
                        >
                            <option value="CONILON">CONILON</option>
                            <option value="KOUILLOI">KOUILLOI</option>
                            <option value="NIAOULI">NIAOULI</option>
                            <option value="UGANDA">UGANDA</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="features">Características</label>

                        <input
                            required
                            type="text"
                            class="form-control mb-1"
                            id="ground_type"
                            v-model="feature_dict.ground_type"
                            placeholder="Tipo de Suelo"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="climate"
                            v-model="feature_dict.climate"
                            placeholder="Clima (Centígrados)"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="brix"
                            v-model="feature_dict.brix"
                            placeholder="Brix"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="mature_test"
                            v-model="feature_dict.mature_test"
                            placeholder="Muestra Cafe Maduro"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="pinton_test"
                            v-model="feature_dict.pinton_test"
                            placeholder="Muestra Cafe Pinton"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="green_test"
                            v-model="feature_dict.green_test"
                            placeholder="Muestra Cafe Verde"
                        />
                        <input
                            required
                            type="number"
                            class="form-control mb-1"
                            id="dried_test"
                            v-model="feature_dict.dried_test"
                            placeholder="Muestra Cafe Seco"
                        />

                        <textarea
                            class="form-control"
                            rows="3"
                            id="more_features"
                            v-model="feature_dict.more_features"
                            placeholder="Mas características"
                        ></textarea>
                    </div>
                    <div class="form-group">
                        <label for="state">Estado</label>
                        <input
                            required
                            disabled
                            type="text"
                            class="form-control"
                            id="state"
                            v-model="batch.state"
                            placeholder="Ingrese el Estado"
                        />
                    </div>
                </div>
                <!-- /.card-body -->

                <div class="card-footer float-right">
                    <button
                        @click="saveBatch"
                        type="submit"
                        class="btn btn-primary"
                    >
                        Crear Lote
                    </button>
                </div>
            </form>
        </div>
    </section>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import BatchDataService from '@/services/BatchDataService';
import Batch from '@/types/Batch';
import ResponseData from '@/types/ResponseData';
import NotifyDataService from '@/services/NotifyDataService';

export default defineComponent({
    name: 'add-batch',
    data() {
        return {
            batch: {
                id: null,
                code: '',
                weight: 0,
                coffe_type: '',
                varieties: '',
                features: '',
                state: '',
                contact_name: '',
                contact: ''
            } as Batch,
            feature_dict: {
                ground_type: '',
                climate: null,
                brix: null,
                mature_test: null,
                pinton_test: null,
                green_test: null,
                dried_test: null,
                more_features: ''
            },
            submitted: false
        };
    },
    methods: {
        saveBatch() {
            let data = {
                code: this.batch.code,
                weight: this.batch.weight,
                coffe_type: this.batch.coffe_type,
                varieties: this.batch.varieties,
                features: this.feature_dict,
                contact: this.batch.contact,
                contact_name: this.batch.contact_name,
                state: this.batch.state
            };
            BatchDataService.create(data)
                .then((response: ResponseData) => {
                    this.batch.id = response.data.id;
                    this.submitted = true;
                })
                .catch((e: Error) => {
                    console.log(e);
                });
            let notify = {
                contact: this.batch.contact,
                message:
                    'Notificación Cafetero su Lote esta en ESTADO RECOLECCION '
            };
            NotifyDataService.send(notify)
                .then((response: ResponseData) => {
                    console.log(response.data);
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        },
        newBatch() {
            this.submitted = false;
            this.batch = {} as Batch;
        }
    },
    created() {
        let result = '';
        const characters =
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        const charactersLength = 8;
        for (let i = 0; i < charactersLength; i++) {
            result += characters.charAt(
                Math.floor(Math.random() * charactersLength)
            );
        }
        this.batch.code = result;
        this.batch.state = 'RECOLECCION';
    }
});
</script>

<style>
#app {
    width: auto !important;
    height: 100vh;
}
</style>