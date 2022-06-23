import {Options, Vue} from 'vue-class-component';
import User from './user/user.vue';

@Options({
    components: {
        'user-dropdown': User
    }
})
export default class Header extends Vue {
    public onToggleMenuSidebar(): void {
        this.$emit('toggle-menu-sidebar');
    }
}
