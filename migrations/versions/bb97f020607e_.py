"""empty message

Revision ID: bb97f020607e
Revises: 
Create Date: 2022-12-13 14:00:15.790771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb97f020607e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('content', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=128), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_comment')
    op.drop_table('blog')
    op.drop_table('user')
    # ### end Alembic commands ###