import "classes/*.pp"

Exec {
    path => "/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin",
}

class drood {

    class {
        init: ;
    }
}

include drood