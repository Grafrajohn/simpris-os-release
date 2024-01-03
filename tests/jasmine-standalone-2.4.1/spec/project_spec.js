describe("Simpris Project:", function() {

    // common js from base template
    window.simpris = { };
    simpris.base_url = "{{ request.META.HTTP_HOST }}";
    simpris.project = { };
    simpris.common = { };
    simpris.report = { };
    simpris.csrf_token = '{{ csrf_token }}';

    //var editor = new FCKEditor( { "parent" : "w2" } );
    //var oEditor1 = FCKeditorAPI.GetInstance('field1');
    CKEDITOR.config.

    it("global namespace not null", function() {
        expect(simpris).not.toBe(null);
    });

    it("Project create", function () {
        var status = simpris.project.post_project_create();
        return false;
    });

    it("Project user create", function () {
        var status = simpris.project.post_project_user_create();
        return false;
    });

    // it("Project delete", function () {
    //     var status = simpris.project.post_project_delete();
    //     return false;
    // });

    it("Project create", function () {
        simpris.project.post_project_user_delete(1);
        return false;
    });

    it("Project edit", function () {
        simpris.project.post_project_edit();
        return false;
    });

    it("Project append user", function () {
        var status = simpris.project.append_project_user();
        return false;
    });

    it("Project validate form", function () {
        var status = simpris.project.validate_project_form('i');
        return false;
    });
});
