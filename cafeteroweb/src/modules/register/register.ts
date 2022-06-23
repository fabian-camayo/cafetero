import {Options, Vue} from 'vue-class-component';
import {
    registerByAuth,
} from '@/services/auth';
import Checkbox from '@/components/checkbox/checkbox.vue';
import Input from '@/components/input/input.vue';
import Button from '@/components/button/button.vue';
import {useToast} from 'vue-toastification';

@Options({
    components: {
        'app-checkbox': Checkbox,
        'app-input': Input,
        'app-button': Button
    }
})
export default class Register extends Vue {
    private appElement: HTMLElement | null = null;
    public email: string = '';
    public password: string = '';
    public rePassword: string = '';
    public agreeTerms: boolean = false;
    public isAuthLoading: boolean = false;

    private toast = useToast();

    public mounted(): void {
        this.appElement = document.getElementById('app') as HTMLElement;
        this.appElement.classList.add('register-page');
    }

    public unmounted(): void {
        (this.appElement as HTMLElement).classList.remove('register-page');
    }

    public async registerByAuth(): Promise<void> {
        try {
            this.isAuthLoading = true;
            const token = await registerByAuth(this.email, this.password);
            this.$store.dispatch('login', token);
            this.toast.success('Register succeeded');
            this.isAuthLoading = false;
        } catch (error: any) {
            this.toast.error(error.message);
            this.isAuthLoading = false;
        }
    }

}