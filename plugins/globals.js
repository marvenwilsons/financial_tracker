import Vue from "vue";

import Widget from '@/components/globals/widget-section'
import WidgetModal from '@/components/globals/widget-modal'
import WidgetContent from '@/components/globals/widget-content'
import WidgetTitle from '@/components/globals/widget-section'

Vue.component("Widget", Widget);
Vue.component("WidgetModal", WidgetModal);
Vue.component("WidgetSection", WidgetContent);
Vue.component("WidgetTitle", WidgetTitle);