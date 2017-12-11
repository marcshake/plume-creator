import qbs
//import plume-creator-data.qbs as Plume

DynamicLibrary {
    name: "plume-creator-data"
    destinationDirectory: "../../lib"

    cpp.defines: [
        "PLUME_CREATOR_DATA_LIBRARY"]
    cpp.includePaths: [ '.']
    //cpp.cxxLanguageVersion: "c++14"
    files: [
        "plmdata.cpp",
        "plmerror.h",
        "plmnotehub.cpp",
        "plmpaperhub.h",
        "plmpropertyhub.cpp",
        "plmsheethub.h",
        "plmdata.h",
        "plmerrorhub.cpp",
        "plmnotehub.h",
        "plmprojecthub.cpp",
        "plmpropertyhub.h",
        "plmsignalhub.h",
        "tasks/plmprojectcloseallprojects.h",
        "tasks/plmprojectcloseproject.h",
        "tasks/plmprojectgetlastloaded.h",
        "tasks/plmprojectgetpath.h",
        "tasks/plmprojectgetprojectidlist.h",
        "tasks/plmprojectloadproject.cpp",
        "tasks/plmprojectloadproject.h",
        "tasks/plmprojectmanager.cpp",
        "tasks/plmprojectmanager.h",
        "tasks/plmprojectsaveproject.h",
        "tasks/plmprojectsaveprojectas.h",
        "tasks/plmprojectsetpath.h",
        "tasks/plmsqlqueries.cpp",
        "tasks/plmsqlqueries.h",
        "tasks/plmsqlstrings.h.autosave",
        "tasks/plmtask.h",
        "tasks/plmtaskerror.cpp",
        "tasks/plmtaskerror.h",
        "tasks/sql/plmexporter.cpp",
        "tasks/sql/plmexporter.h",
        "tasks/sql/plmimporter.cpp",
        "tasks/sql/plmimporter.h",
        "tasks/sql/plmproject.cpp",
        "tasks/sql/plmproject.h",
        "tasks/sql/plmproperty.cpp",
        "tasks/sql/plmproperty.h",
        "tasks/sql/plmupgrader.cpp",
        "tasks/sql/plmupgrader.h",
        "tasks/sql/tree/plmdberror.h",
        "tasks/sql/tree/plmdbpaper.cpp",
        "tasks/sql/tree/plmdbpaper.h",
        "tasks/sql/tree/plmdbtree.cpp",
        "tasks/sql/tree/plmdbtree.h",
        "tasks/sql/tree/plmnotetree.cpp",
        "tasks/sql/tree/plmnotetree.h",
        "tasks/sql/tree/plmsheettree.cpp",
        "tasks/sql/tree/plmsheettree.h",
        "tasks/sql/tree/plmtree.cpp",
        "tasks/sql/tree/plmtree.h",
        "tools.h",
        "plmerror.cpp",
        "plmerrorhub.h",
        "plmpaperhub.cpp",
        "plmprojecthub.h",
        "plmsheethub.cpp",
        "plume_creator_data_global.h"
    ]

    Depends { name: "Qt"; submodules: ["core", "sql"]}
    Depends { name: "cpp" }
    cpp.optimization: "fast"

    Export {
        Depends { name: "cpp" }
        cpp.includePaths: [product.sourceDirectory]
    }

    Depends { name: "Android.ndk" }
    Android.ndk.appStl: "gnustl_shared"
}
