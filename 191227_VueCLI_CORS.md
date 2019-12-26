# VueCLI CORS 처리하기

- Vue.js에서 request, XMLHttpRequest 등의 객체를 통해 다른 서버에 요청을 보낼 경우 CORS Error로 인해 어려움을 겪었다.
- 이에, 선생님에 도움을 요청하였고 몇 가지 해결책을 받아 시도해보았다.

## Vue 자체 설정을 통한 해결법

- [참고 사이트](https://medium.com/js-dojo/how-to-deal-with-cors-error-on-vue-cli-3-d78c024ce8d3)

1. 먼저 Ajax 요청을 이용하는데, Ajax를 요청하는 domain과 vue application의 domain을 같게 설정해줘야 한다.
   - Vue CLI 프로젝트에 github page 배포를 위한 `vue.config.js` 파일을 만들었었다.
   - 이 파일을 다음과 같이 backend server의 도메인을 추가해준다.

```javascript
devServer: {
        proxy: '<backend domain>',
    }
```



