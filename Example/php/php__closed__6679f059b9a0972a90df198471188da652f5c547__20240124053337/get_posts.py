'''
Core Post API
@package WordPress
@subpackage Post
'''
# Post Type registration.
def create_initial_post_types():
    WP_Post_Type.reset_default_labels()
    register_post_type(
        'post',
        {
            'labels': {
                'name_admin_bar': _x('Post', 'add new from admin bar'),
            },
            'public': True,
            '_builtin': True,  # internal use only. don't use this when registering your own post type.
            '_edit_link': 'post.php?post=%d',  # internal use only. don't use this when registering your own post type.
            'capability_type': 'post',
            'map_meta_cap': True,
            'menu_position': 5,
            'menu_icon': 'dashicons-admin-post',
            'hierarchical': False,
            'rewrite': False,
            'query_var': False,
            'delete_with_user': True,
            'supports': ['title', 'editor', 'author', 'thumbnail', 'excerpt', 'trackbacks', 'custom-fields', 'comments', 'revisions', 'post-formats'],
            'show_in_rest': True,
            'rest_base': 'posts',
            'rest_controller_class': 'WP_REST_Posts_Controller',
        }
    )
    register_post_type(
        'page',
        {
            'labels': {
                'name_admin_bar': _x('Page', 'add new from admin bar'),
            },
            'public': True,
            'publicly_queryable': False,
            '_builtin': True,  # internal use only. don't use this when registering your own post type.
            '_edit_link': 'post.php?post=%d',  # internal use only. don't use this when registering your own post type.
            'capability_type': 'page',
            'map_meta_cap': True,
            'menu_position': 20,
            'menu_icon': 'dashicons-admin-page',
            'hierarchical': True,
            'rewrite': False,
            'query_var': False,
            'delete_with_user': True,
            'supports': ['title', 'editor', 'author', 'thumbnail', 'page-attributes', 'custom-fields', 'comments', 'revisions'],
            'show_in_rest': True,
            'rest_base': 'pages',
            'rest_controller_class': 'WP_REST_Posts_Controller',
        }
    )
    register_post_type(
        'attachment',
        {
            'labels': {
                'name': _x('Media', 'post type general name'),
                'name_admin_bar': _x('Media', 'add new from admin bar'),
                'add_new': __('Add New Media File'),
                'edit_item': __('Edit Media'),
                'view_item': ('1' === get_option('wp_attachment_pages_enabled')) ? __('View Attachment Page') : __('View Media File'),
                'attributes': __('Attachment Attributes'),
            },
            'public': True,
            'show_ui': True,
            '_builtin': True,  # internal use only. don't use this when registering your own post type.
            '_edit_link': 'post.php?post=%d',  # internal use only. don't use this when registering your own post type.
            'capability_type': 'post',
            'capabilities': {
                'create_posts': 'upload_files',
            },
        }
    )
'''
COMMIT