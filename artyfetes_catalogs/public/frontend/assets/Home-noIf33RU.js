import{c as d,r as u,u as r,o as e,a as t,F as n,b as _,d as l,w as m,e as p,t as g,f}from"./index-DhEIjAEx.js";const x={key:0},y={key:1,class:"mt-10 space-y-12 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 lg:gap-12 lg:space-y-0"},h={__name:"CatalogList",setup(i){const a=d({doctype:"Catalog",fields:["title","name"],filters:[["isactive","=",1],["isvisible","=",1],["type","=","Catalog"]],auto:!0});return a.fetch(),(s,v)=>{const c=u("router-link");return r(a).loading?(e(),t("div",x,"Chargement des catalogues...")):(e(),t("div",y,[(e(!0),t(n,null,_(r(a).data,o=>(e(),t("div",{key:o.name},[l(c,{to:{name:"Catalog",params:{catalogid:o.title}},class:"bg-secondary text-primary text-center aspect-[10/15] text-2xl font-bold items-center justify-center flex hover:transform hover:scale-105 transition duration-300 ease-in-out hover:shadow-[0_35px_35px_rgba(0,0,0,0.25)]"},{default:m(()=>[p(g(o.title),1)]),_:2},1032,["to"])]))),128))]))}}},C={__name:"Home",setup(i){return(a,s)=>(e(),t(n,null,[s[0]||(s[0]=f("h1",null,"Tous les catalogues",-1)),l(h)],64))}};export{C as default};
